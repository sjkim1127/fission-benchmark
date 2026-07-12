/* Lightweight control-flow flattening toy (adversarial track fixture). */
#include <stdint.h>

int cff_classify(int x) {
    int state = 0;
    int result = 0;
    for (;;) {
        switch (state) {
        case 0:
            state = (x < 0) ? 1 : 2;
            break;
        case 1:
            result = -1;
            state = 3;
            break;
        case 2:
            state = (x == 0) ? 4 : 5;
            break;
        case 4:
            result = 0;
            state = 3;
            break;
        case 5:
            result = 1;
            state = 3;
            break;
        case 3:
            return result;
        default:
            return 99;
        }
    }
}

int main(void) {
    return cff_classify(3) + cff_classify(-1) + cff_classify(0);
}
