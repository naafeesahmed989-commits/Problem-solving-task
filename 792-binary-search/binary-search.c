int search(int* nums, int numsSize, int target) {
    int mid;
    int low=0;
    int high= numsSize-1;
    int found=-1;
    while(low<=high){
        mid = (low+high)/2;
        if(nums[mid]==target){
            found=mid;
            
            break;
        }
        else if(nums[mid]<target){
            low=mid+1;
        }
        else{
           high=mid-1;
        }
    }
    if(found==-1){
       
    }
    return found;
}