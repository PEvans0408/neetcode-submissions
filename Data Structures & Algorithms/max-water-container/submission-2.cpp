class Solution {
public:
    int maxArea(vector<int>& heights) {
        int candidateleft = 0;
        int candidateright = heights.size() - 1;
        int lower_bar = (heights[candidateleft] <= heights[candidateright]) ? heights[candidateleft] : heights[candidateright];
        int candidate_area = lower_bar * (candidateright - candidateleft);
        int greatest_area = candidate_area;
        while (candidateleft < candidateright) {
            if (lower_bar == heights[candidateleft]) {
                candidateleft++;
                lower_bar = (heights[candidateleft] <= heights[candidateright]) ? heights[candidateleft] : heights[candidateright];
                candidate_area = lower_bar * (candidateright - candidateleft);
                if (candidate_area >= greatest_area) {
                    greatest_area = candidate_area;
                }
            } else {
                candidateright--;
                lower_bar = (heights[candidateleft] <= heights[candidateright]) ? heights[candidateleft] : heights[candidateright];
                candidate_area = lower_bar * (candidateright - candidateleft);
                if (candidate_area >= greatest_area) {
                    greatest_area = candidate_area;
                }
            }
        }
        return greatest_area;
    }
};
