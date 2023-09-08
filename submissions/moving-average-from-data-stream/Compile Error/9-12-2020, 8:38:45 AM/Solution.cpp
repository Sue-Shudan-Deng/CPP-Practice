// https://leetcode.com/problems/moving-average-from-data-stream

class MovingAverage {
    
private:
    queue<int> data;
    int s_;
public:
    /** Initialize your data structure here. */
    MovingAverage(int size) {
        s_ = size;
    }
    double next(int val) {
        if (s_ == data.size()) {
            data.pop();
            data.push(val);
        }
        double sum = static_cast<double>std::accumulate(data.begin(), data.end(), 0);
        return sum / data.size();
    }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */