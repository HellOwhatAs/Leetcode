#
# @lc app=leetcode.cn id=2532 lang=python3
#
# [2532] 过桥的时间
#

# @lc code=start
from typing import List
from functools import cmp_to_key
from math import inf, isinf

try:
    import cppyy
    cppyy.cppexec('''
    #include<vector>
    #include<queue>
    using namespace std;
    class Solution {
    public:
        using PII = pair<int, int>;
        int findCrossingTime(int n, int k, const vector<vector<int>>& time) {
            // 定义等待中的工人优先级比较规则，时间总和越高，效率越低，优先级越低，越优先被取出
            auto wait_priority_cmp = [&](int x, int y) {
                int time_x = time[x][0] + time[x][2];
                int time_y = time[y][0] + time[y][2];
                return time_x != time_y ? time_x < time_y : x < y;
            };

            priority_queue<int, vector<int>, decltype(wait_priority_cmp)> wait_left(wait_priority_cmp), wait_right(wait_priority_cmp);

            priority_queue<PII, vector<PII>, greater<PII>> work_left, work_right;

            int remain = n, cur_time = 0;
            for (int i = 0; i < k; i++) {
                wait_left.push(i);
            }
            while (remain > 0 || !work_right.empty() || !wait_right.empty()) {
                // 1. 若 work_left 或 work_right 中的工人完成工作，则将他们取出，并分别放置到 wait_left 和 wait_right 中。
                while (!work_left.empty() && work_left.top().first <= cur_time) {
                    wait_left.push(work_left.top().second);
                    work_left.pop();
                }
                while (!work_right.empty() && work_right.top().first <= cur_time) {
                    wait_right.push(work_right.top().second);
                    work_right.pop();
                }

                if (!wait_right.empty()) {
                    // 2. 若右侧有工人在等待，则取出优先级最低的工人并过桥
                    int id = wait_right.top();
                    wait_right.pop();
                    cur_time += time[id][2];
                    work_left.push({cur_time + time[id][3], id});
                } else if (remain > 0 && !wait_left.empty()) {
                    // 3. 若右侧还有箱子，并且左侧有工人在等待，则取出优先级最低的工人并过桥
                    int id = wait_left.top();
                    wait_left.pop();
                    cur_time += time[id][0];
                    work_right.push({cur_time + time[id][1], id});
                    remain--;
                } else {
                    // 4. 否则，没有人需要过桥，时间过渡到 work_left 和 work_right 中的最早完成时间
                    int next_time = INT_MAX;
                    if (!work_left.empty()) {
                        next_time = min(next_time, work_left.top().first);
                    }
                    if (!work_right.empty()) {
                        next_time = min(next_time, work_right.top().first);
                    }
                    if (next_time != INT_MAX) {
                        cur_time = max(next_time, cur_time);
                    }
                }
            }
            return cur_time;
        }
    };
    ''')
    findCrossingTime = cppyy.gbl.Solution().findCrossingTime
except:
    findCrossingTime = None

class heapq:

    @staticmethod
    def heappush(heap, item, key = None):
        """Push item onto heap, maintaining the heap invariant."""
        heap.append(item)
        heapq._siftdown(heap, 0, len(heap)-1, key)
    @staticmethod
    def heappop(heap, key = None):
        """Pop the smallest item off the heap, maintaining the heap invariant."""
        lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
        if heap:
            returnitem = heap[0]
            heap[0] = lastelt
            heapq._siftup(heap, 0, key)
            return returnitem
        return lastelt
    @staticmethod
    def heapreplace(heap, item, key = None):
        """Pop and return the current smallest value, and add the new item.

        This is more efficient than heappop() followed by heappush(), and can be
        more appropriate when using a fixed-size heap.  Note that the value
        returned may be larger than item!  That constrains reasonable uses of
        this routine unless written as part of a conditional replacement:

            if item > heap[0]:
                item = heapreplace(heap, item)
        """
        returnitem = heap[0]    # raises appropriate IndexError if heap is empty
        heap[0] = item
        heapq._siftup(heap, 0, key)
        return returnitem
    @staticmethod
    def heappushpop(heap, item, key = None):
        """Fast version of a heappush followed by a heappop."""
        if heap and heap[0] < item:
            item, heap[0] = heap[0], item
            heapq._siftup(heap, 0, key)
        return item
    @staticmethod
    def heapify(x, key = None):
        """Transform list into a heap, in-place, in O(len(x)) time."""
        n = len(x)
        # Transform bottom-up.  The largest index there's any point to looking at
        # is the largest with a child index in-range, so must have 2*i + 1 < n,
        # or i < (n-1)/2.  If n is even = 2*j, this is (2*j-1)/2 = j-1/2 so
        # j-1 is the largest, which is n//2 - 1.  If n is odd = 2*j+1, this is
        # (2*j+1-1)/2 = j so j-1 is the largest, and that's again n//2-1.
        for i in reversed(range(n//2)):
            heapq._siftup(x, i, key)
    @staticmethod
    def _heappop_max(heap, key = None):
        """Maxheap version of a heappop."""
        lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
        if heap:
            returnitem = heap[0]
            heap[0] = lastelt
            heapq._siftup_max(heap, 0, key)
            return returnitem
        return lastelt
    @staticmethod
    def _heapreplace_max(heap, item, key = None):
        """Maxheap version of a heappop followed by a heappush."""
        returnitem = heap[0]    # raises appropriate IndexError if heap is empty
        heap[0] = item
        heapq._siftup_max(heap, 0, key)
        return returnitem
    @staticmethod
    def _heapify_max(x, key = None):
        """Transform list into a maxheap, in-place, in O(len(x)) time."""
        n = len(x)
        for i in reversed(range(n//2)):
            heapq._siftup_max(x, i, key)

    @staticmethod
    def _siftdown(heap, startpos, pos, key = None):
        newitem = heap[pos]

        if not key is None:
            keynewitem = key(newitem)
            while pos > startpos:
                parentpos = (pos - 1) >> 1
                parent = heap[parentpos]
                if keynewitem < key(parent):
                    heap[pos] = parent
                    pos = parentpos
                    continue
                break
            heap[pos] = newitem
            return

        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = heap[parentpos]
            if newitem < parent:
                heap[pos] = parent
                pos = parentpos
                continue
            break
        heap[pos] = newitem

    @staticmethod
    def _siftup(heap, pos, key = None):
        endpos = len(heap)
        startpos = pos
        newitem = heap[pos]

        if not key is None:
            # Bubble up the smaller child until hitting a leaf.
            childpos = 2*pos + 1    # leftmost child position
            while childpos < endpos:
                # Set childpos to index of smaller child.
                rightpos = childpos + 1
                if rightpos < endpos and not key(heap[childpos]) < key(heap[rightpos]):
                    childpos = rightpos
                # Move the smaller child up.
                heap[pos] = heap[childpos]
                pos = childpos
                childpos = 2*pos + 1
            # The leaf at pos is empty now.  Put newitem there, and bubble it up
            # to its final resting place (by sifting its parents down).
            heap[pos] = newitem
            heapq._siftdown(heap, startpos, pos, key)
            return

        # Bubble up the smaller child until hitting a leaf.
        childpos = 2*pos + 1    # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not heap[childpos] < heap[rightpos]:
                childpos = rightpos
            # Move the smaller child up.
            heap[pos] = heap[childpos]
            pos = childpos
            childpos = 2*pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        heap[pos] = newitem
        heapq._siftdown(heap, startpos, pos)

    @staticmethod
    def _siftdown_max(heap, startpos, pos, key = None):
        'Maxheap variant of _siftdown'
        newitem = heap[pos]

        if not key is None:
            keynewitem = key(newitem)
            # Follow the path to the root, moving parents down until finding a place
            # newitem fits.
            while pos > startpos:
                parentpos = (pos - 1) >> 1
                parent = heap[parentpos]
                if key(parent) < keynewitem:
                    heap[pos] = parent
                    pos = parentpos
                    continue
                break
            heap[pos] = newitem
            return

        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = heap[parentpos]
            if parent < newitem:
                heap[pos] = parent
                pos = parentpos
                continue
            break
        heap[pos] = newitem
    @staticmethod
    def _siftup_max(heap, pos, key = None):
        'Maxheap variant of _siftup'
        endpos = len(heap)
        startpos = pos
        newitem = heap[pos]

        if not key is None:
            # Bubble up the larger child until hitting a leaf.
            childpos = 2*pos + 1    # leftmost child position
            while childpos < endpos:
                # Set childpos to index of larger child.
                rightpos = childpos + 1
                if rightpos < endpos and not key(heap[rightpos]) < key(heap[childpos]):
                    childpos = rightpos
                # Move the larger child up.
                heap[pos] = heap[childpos]
                pos = childpos
                childpos = 2*pos + 1
            # The leaf at pos is empty now.  Put newitem there, and bubble it up
            # to its final resting place (by sifting its parents down).
            heap[pos] = newitem
            heapq._siftdown_max(heap, startpos, pos, key)
            return

        # Bubble up the larger child until hitting a leaf.
        childpos = 2*pos + 1    # leftmost child position
        while childpos < endpos:
            # Set childpos to index of larger child.
            rightpos = childpos + 1
            if rightpos < endpos and not heap[rightpos] < heap[childpos]:
                childpos = rightpos
            # Move the larger child up.
            heap[pos] = heap[childpos]
            pos = childpos
            childpos = 2*pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        heap[pos] = newitem
        heapq._siftdown_max(heap, startpos, pos)


class Solution:
    
    def wait_priority_cmp(self, x: int, y: int):
        time_x = self.time[x][0] + self.time[x][2]
        time_y = self.time[y][0] + self.time[y][2]
        if (time_x < time_y if time_x != time_y else x < y): return 1
        if x == y: return 0
        return -1

    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        if findCrossingTime is not None: return findCrossingTime(n, k, time)
        self.time = time
        wait_left, wait_right = list(range(k)), []
        work_left, work_right = [], []
        remain, cur_time = n, 0
        key = cmp_to_key(self.wait_priority_cmp)
        heapq.heapify(wait_left, key=key)
        while remain > 0 or work_right or wait_right:
            while work_left and work_left[0][0] <= cur_time:
                heapq.heappush(wait_left, work_left[0][1], key=key)
                heapq.heappop(work_left)
            while work_right and work_right[0][0] <= cur_time:
                heapq.heappush(wait_right, work_right[0][1], key=key)
                heapq.heappop(work_right)
            
            if wait_right:
                id = heapq.heappop(wait_right, key=key)
                cur_time += time[id][2]
                heapq.heappush(work_left, (cur_time + time[id][3], id))
            elif remain > 0 and wait_left:
                id = heapq.heappop(wait_left, key=key)
                cur_time += time[id][0]
                heapq.heappush(work_right, (cur_time + time[id][1], id))
                remain -= 1
            else:
                next_time = inf
                if work_left:
                    next_time = min(next_time, work_left[0][0])
                if work_right:
                    next_time = min(next_time, work_right[0][0])
                if not isinf(next_time):
                    cur_time = max(next_time, cur_time)
        return cur_time



# @lc code=end

print(Solution().findCrossingTime(n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]))
print(Solution().findCrossingTime(n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]]))
print(Solution().findCrossingTime(10, 6, [[2,10,5,8],[3,5,2,2],[5,8,10,10],[7,8,8,5],[5,6,6,10],[6,10,6,2]]))