//
简单的计数排序
//
void sortColors(int* nums, int numsSize)
{
    int a[3] = {0};
    for(int i = 0; i<numsSize;i++)
{
    a[nums[i]]+= 1;
}
 int j = 0;
for(int i = 0;i<3;i++)
{
    while(a[i] > 0)
    {
    nums[j++] =i;
    a[i]--;
    }
}
}
