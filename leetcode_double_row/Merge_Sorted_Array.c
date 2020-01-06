//
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
解题思路:
想到了归并排序的合并操作
失误:
一:没有考虑极端情况,比如数组二为空
二:对或操作不熟悉,C语言的或操作值比较前面的
三:控制条件考虑不清楚
//
void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n)
{
    if(n!=0)
    {
    int * nums = (int *)malloc(sizeof(int)*m);//未考虑到要分配内存,代码敏感度不够
    for(int i = 0;i < m;i++)
    {
        nums[i] = nums1[i];
    }
    int a = 0;
    int b= 0;
    for(int i = 0;i<m+n;i++)
    {
        if(a < m && (b>n-1 || nums[a] < nums[b])) 
        {
            nums1[i] = nums[a++]; 
            continue;
        }
        if( b < n &&(nums2[b] <= nums[a] || a> m-1))
        {
            nums1[i] = nums2[b++];
        }
    }
    free(nums);
    }
}
