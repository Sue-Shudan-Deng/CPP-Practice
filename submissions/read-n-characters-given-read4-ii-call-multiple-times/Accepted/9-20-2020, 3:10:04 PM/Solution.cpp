// https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times

/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char *buf4);
 */

class Solution {

private:
    int pointer = 0, len = 0;
    char* buf4 = new char[4];
    
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) {
        int index = 0;
        while (index < n) {
            // read
            if (pointer == 0) {
                len = read4(buf4);
                if (len == 0) {
                    break;
                }
            }
            // copy
            while (index < n && pointer < len) {
                buf[index] = buf4[pointer];
                ++pointer;
                ++index;
            }
            if (len < 4) {
                break;
            }
            if (pointer == len) {
                pointer = 0;
            }
        }
        return index;
    }
};