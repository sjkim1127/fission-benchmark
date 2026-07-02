"""Mermaid CFG generator and color-coding utility."""
from __future__ import annotations

from typing import Any

def canonicalize_addr(addr: Any) -> str:
    if addr is None:
        return ""
    if isinstance(addr, int):
        return f"0x{addr:x}"
    addr_str = str(addr).strip().lower()
    if not addr_str:
        return ""
    try:
        if addr_str.startswith("0x"):
            val = int(addr_str, 16)
        else:
            val = int(addr_str, 16)
        return f"0x{val:x}"
    except ValueError:
        return addr_str

def escape_mermaid(text: str) -> str:
    if not isinstance(text, str):
        text = str(text)
    return (
        text.replace('&', '&amp;')
        .replace('"', '&quot;')
        .replace('<', '&lt;')
        .replace('>', '&gt;')
        .replace('[', '&#91;')
        .replace(']', '&#93;')
    )

def make_node_id(addr: str) -> str:
    clean = "".join(c if c.isalnum() else "_" for c in addr)
    return f"B_{clean}"

def generate_mermaid(cfg: dict | None, other_cfg: dict | None) -> str:
    if not cfg or (not cfg.get("blocks") and not cfg.get("edges")):
        return "graph TD\n    empty[\"Empty CFG\"]"

    blocks = cfg.get("blocks", [])
    if not isinstance(blocks, list):
        blocks = []

    blocks_map = {}
    for b in blocks:
        if not isinstance(b, dict):
            continue
        addr = canonicalize_addr(b.get("addr", b.get("start")))
        if addr:
            blocks_map[addr] = b

    other_blocks_map = {}
    if other_cfg and isinstance(other_cfg, dict):
        other_blocks = other_cfg.get("blocks", [])
        if isinstance(other_blocks, list):
            for b in other_blocks:
                if not isinstance(b, dict):
                    continue
                addr = canonicalize_addr(b.get("addr", b.get("start")))
                if addr:
                    other_blocks_map[addr] = b

    edges_list = []
    edges = cfg.get("edges", [])
    if isinstance(edges, list):
        for e in edges:
            if not isinstance(e, dict):
                continue
            src = canonicalize_addr(e.get("src", e.get("source")))
            dst = canonicalize_addr(e.get("dst", e.get("target")))
            if src and dst:
                edges_list.append((src, dst))

    other_edges_set = set()
    if other_cfg and isinstance(other_cfg, dict):
        other_edges = other_cfg.get("edges", [])
        if isinstance(other_edges, list):
            for e in other_edges:
                if not isinstance(e, dict):
                    continue
                src = canonicalize_addr(e.get("src", e.get("source")))
                dst = canonicalize_addr(e.get("dst", e.get("target")))
                if src and dst:
                    other_edges_set.add((src, dst))

    # All nodes mentioned in blocks or edges
    all_nodes = set(blocks_map.keys())
    for src, dst in edges_list:
        all_nodes.add(src)
        all_nodes.add(dst)

    lines = ["graph TD"]

    # Write node declarations
    for addr in sorted(all_nodes):
        node_id = make_node_id(addr)
        if addr in blocks_map:
            b = blocks_map[addr]
            size = b.get("size")
            instructions = b.get("instructions", [])
            if not isinstance(instructions, list):
                instructions = []
            
            label_parts = [addr]
            if size is not None:
                label_parts.append(f"{size} bytes")
            if instructions:
                label_parts.extend(instructions)
            
            escaped_parts = [escape_mermaid(part) for part in label_parts]
            label = "<br/>".join(escaped_parts)
        else:
            label = escape_mermaid(addr)

        lines.append(f'    {node_id}["{label}"]')

    # Apply node styles
    for addr in sorted(all_nodes):
        node_id = make_node_id(addr)
        if addr not in blocks_map:
            # present in edges but not blocks in this graph -> missing node -> Red/Orange
            lines.append(f"    style {node_id} fill:#ffcccc,stroke:#ff0000")
        elif addr not in other_blocks_map:
            # present in this but missing in other -> Red/Orange
            lines.append(f"    style {node_id} fill:#ffcccc,stroke:#ff0000")
        else:
            b = blocks_map[addr]
            ob = other_blocks_map[addr]
            
            # Compare instructions and size
            b_size = b.get("size")
            ob_size = ob.get("size")
            b_inst = b.get("instructions", [])
            ob_inst = ob.get("instructions", [])
            if not isinstance(b_inst, list):
                b_inst = []
            if not isinstance(ob_inst, list):
                ob_inst = []

            if b_size == ob_size and b_inst == ob_inst:
                # Perfectly identical block structures and instruction counts -> Gray/Green
                lines.append(f"    style {node_id} fill:#d5e8d4,stroke:#82b366")
            else:
                # Matching block addresses, but with content differences -> Yellow/Orange
                lines.append(f"    style {node_id} fill:#fff2cc,stroke:#d6b656")

    # Write edges
    link_styles = []
    for idx, (src, dst) in enumerate(edges_list):
        src_id = make_node_id(src)
        dst_id = make_node_id(dst)
        lines.append(f"    {src_id} --> {dst_id}")
        
        # Check if edge is missing in the other graph -> Red/Orange
        if (src, dst) not in other_edges_set:
            link_styles.append(f"    linkStyle {idx} stroke:#ff5555,stroke-width:2px;")

    # Append edge styles
    lines.extend(link_styles)

    return "\n".join(lines)
