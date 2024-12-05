def merge(nums1,nums2,m,n):
    i=m-1
    j=n-1
    last=m+n-1
    
    while i >=0 and j >=0 :
        if nums1[i] >= nums2[j]:
            nums1[last]=nums1[i]
            i-=1
        else:
            nums1[last]=nums2[j]
            j-=1
        last-=1
        
    while j >=0:
        nums1[last]=nums2[j]
        j-=1
        last-=1
        
    print(nums1)
    
arr1=[1,2,3,0,0,0,0,0,0,0,0]
arr2=[1,2,4,5,6,8,90,899,9000]
m=3
n=7


merge(arr1,arr2,m,n)
