#include<iostream>
#include<vector>
#include<climits>
using namespace std;
void display(const vector<int> arr){
    for(int num : arr){
        cout<<num<<" ";
    }
    cout<<endl;
}
void swap(int *a,int *b){
    int temp=*a;
    *a=*b;
    *b=temp;
}
void sort(vector<vector<int> > cumsum){
    for(int i=0;i<cumsum.size();i++){
        for(int j=0;j<cumsum.size()-i-1;j++){
            if(cumsum[j][0]>cumsum[j+1][0]){
                swap(cumsum[j],cumsum[j+1]);
            }
        }
    }
}
int findIndex(vector<vector<int>>& cumSum,int val){
    int low=0;
    int high=cumSum.size()-1;
    while(low<high){
        int mid=low+(low+high)/2;
        if(cumSum[mid][0]<=val){
            low=mid+1;
    }
    else{
        high=mid;
    }
    
}
return cumSum[low][0]==val?low:-1;
}
int findMinimumSubArray(const vector<int> arr,int k){
    vector<vector<int>> cumSum;
    for (int i=0;i<arr.size();i++){
        cumSum.push_back({arr[i],i});
    }
    sort(cumSum);
    vector<int> minIndex(arr.size());
    minIndex[0]=cumSum[0][1];
    for (int i=1;i<arr.size();i++){
        minIndex[i]=min(minIndex[i-1],cumSum[i][1]);
    }
    int sum=0;
    int result=0;
    for (int i=0;i<arr.size();i++){
        sum+=arr[i];
        if(sum<k){
            result=min(result,i+1);
        }
        else{
            int index=findIndex(cumSum,sum-k);
            if(index!=-1 && minIndex[index]<i){
                result=min(result,i-minIndex[index]);
            }
        }
    }

}
int main() {
    vector<int> arr = {2, -3, 3, 2, 0, -1};
    
    int k = 3;

    display(arr);
    int x=findMinimumSubArray(arr,k);
    cout << "Smallest subarray having sum less than " << k << " = " << endl;
    cout<<x<<endl;
    return 0;
}