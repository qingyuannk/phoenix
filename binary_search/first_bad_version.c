### 解题思路
此处撰写解题思路

### 代码

// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

int firstBadVersion(int n) 
{
        int lo = 1;
        int high = n;
         int middle;
        while(lo<= high)
        {
            middle = lo + (high-lo)/2;//防止溢出
            //middle = (lo+high)/2;
            if(isBadVersion(middle))
            {
                high = middle-1;
            }
            else
            {
                lo =middle +1;
            }
        }
        return lo;
}

