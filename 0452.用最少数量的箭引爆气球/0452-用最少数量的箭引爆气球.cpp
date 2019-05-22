

#include <algorithm>
#include <vector>

bool cmp(const std::pair<int, int> &a, const std::pair<int ,int> &b) {
    return a.first < b.first;
}

class Solution {
public:
    int findMinArrowShots(std::vector<std::pair<int, int> >& points) {
    	if (points.size() == 0){
	    	return 0;
	    }
    	std::sort(points.begin(), points.end(), cmp);
    	int shoot_num = 1;
    	int shoot_begin = points[0].first;
    	int shoot_end = points[0].second;
    	for (int i = 1; i < points.size(); i++){
	    	if (points[i].first <= shoot_end){
	    		shoot_begin = points[i].first;
    			if (shoot_end > points[i].second){
			    	shoot_end = points[i].second;
			    }
	    	}
	    	else{
	    		shoot_num++;
	    		shoot_begin = points[i].first;
	    		shoot_end = points[i].second;
	    	}
	    }
	    return shoot_num;
    }
};