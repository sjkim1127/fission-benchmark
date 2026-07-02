from runner.graph_utils import generate_mermaid, canonicalize_addr, escape_mermaid, make_node_id

def test_extreme_and_malformed_inputs():
    # 1. Empty blocks, empty edges
    cfg_empty = {"blocks": [], "edges": []}
    other_cfg_empty = {"blocks": [], "edges": []}
    res = generate_mermaid(cfg_empty, other_cfg_empty)
    assert "graph TD" in res
    assert 'empty["Empty CFG"]' in res

    # 2. None / falsy inputs
    res_none = generate_mermaid(None, None)
    assert "graph TD" in res_none
    assert 'empty["Empty CFG"]' in res_none

    res_empty_dict = generate_mermaid({}, {})
    assert "graph TD" in res_empty_dict
    assert 'empty["Empty CFG"]' in res_empty_dict

    # 3. Missing start/end/addr addresses in blocks
    cfg_missing_addr = {
        "blocks": [
            {"size": 10},
            {"instructions": ["nop"]}
        ],
        "edges": []
    }
    res = generate_mermaid(cfg_missing_addr, None)
    assert "graph TD" in res

    # 4. Cycle loops (e.g. A -> B -> C -> A)
    cfg_cycle = {
        "blocks": [
            {"addr": "0x1000", "size": 10},
            {"addr": "0x2000", "size": 20},
            {"addr": "0x3000", "size": 30}
        ],
        "edges": [
            {"src": "0x1000", "dst": "0x2000"},
            {"src": "0x2000", "dst": "0x3000"},
            {"src": "0x3000", "dst": "0x1000"}
        ]
    }
    res = generate_mermaid(cfg_cycle, cfg_cycle)
    assert "graph TD" in res
    assert "B_0x1000 --> B_0x2000" in res
    assert "B_0x2000 --> B_0x3000" in res
    assert "B_0x3000 --> B_0x1000" in res

    # 5. Single block graph (no edges)
    cfg_single = {
        "blocks": [{"addr": "0x1000", "size": 5}],
        "edges": []
    }
    res = generate_mermaid(cfg_single, None)
    assert "graph TD" in res
    assert 'B_0x1000["0x1000<br/>5 bytes"]' in res

    # 6. Empty edges or missing src/dst in edges
    cfg_empty_edges = {
        "blocks": [{"addr": "0x1000"}, {"addr": "0x2000"}],
        "edges": [
            {"src": "0x1000"},
            {"dst": "0x2000"},
            {},
            {"src": "0x1000", "dst": None},
            {"src": None, "dst": "0x2000"}
        ]
    }
    res = generate_mermaid(cfg_empty_edges, None)
    assert "graph TD" in res
    assert "-->" not in res

    # 7. Malformed data types (e.g. blocks is a string, edges is an integer, non-dict elements)
    cfg_malformed_types = {
        "blocks": "not-a-list",
        "edges": 12345
    }
    res = generate_mermaid(cfg_malformed_types, None)
    assert "graph TD" in res

    cfg_malformed_list_elements = {
        "blocks": ["not-a-dict", 123, None],
        "edges": ["not-a-dict", 123, None]
    }
    res = generate_mermaid(cfg_malformed_list_elements, None)
    assert "graph TD" in res

    # 8. Non-hex, alphanumeric, empty, or special characters in addresses
    cfg_special_addrs = {
        "blocks": [
            {"addr": "main", "size": 10},
            {"addr": "0x1000; drop table; --", "size": 20},
            {"addr": "  ", "size": 30}
        ],
        "edges": [
            {"src": "main", "dst": "0x1000; drop table; --"}
        ]
    }
    res = generate_mermaid(cfg_special_addrs, None)
    assert "graph TD" in res
    assert 'B_main["main<br/>10 bytes"]' in res
    assert 'B_main --> B_0x1000__drop_table____' in res

def test_canonicalize_addr_edge_cases():
    assert canonicalize_addr(None) == ""
    assert canonicalize_addr(0x100) == "0x100"
    assert canonicalize_addr("  0x200  ") == "0x200"
    assert canonicalize_addr("300") == "0x300"
    assert canonicalize_addr("abc") == "0xabc"
    assert canonicalize_addr("xyz") == "xyz"
    assert canonicalize_addr("") == ""

def test_escape_mermaid_edge_cases():
    # Correct order of replacements in escape_mermaid prevents double-escaping:
    assert escape_mermaid('"hello"') == "&quot;hello&quot;"
    assert escape_mermaid("<tag>") == "&lt;tag&gt;"
    # 'a & b' -> 'a &amp; b'
    assert escape_mermaid("a & b") == "a &amp; b"
    # '[brackets]' -> '&#91;brackets&#93;'
    assert escape_mermaid("[brackets]") == "&#91;brackets&#93;"
    assert escape_mermaid(123) == "123"

def test_make_node_id_edge_cases():
    assert make_node_id("0x1000") == "B_0x1000"
    assert make_node_id("B_1000") == "B_B_1000"
    assert make_node_id("addr-with-dash") == "B_addr_with_dash"
    assert make_node_id("!@#$") == "B_____"
