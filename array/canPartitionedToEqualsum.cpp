#include<iostream>
using namespace std;
void canPartitionToEqualSum(int *arr,int n){
    int sum=0;
    for (int i = 0; i < n; i++)
    {
        sum+=arr[i];
    }
   
    if(sum%2!=0){
        cout<<"Cannot be partitioned into two subsets with equal sum."<<endl;
        return;
    }
     int target=sum/2;
    bool dp[n+1][target+1] = {false};
    dp[0][0] = true;
    for (int i = 1; i <= n; i++) {
        dp[i][0] = true;
    }

    for(int i=1;i<=n;i++){
        for(int j=1;j<=target;j++){            
            if (arr[i - 1] <= j) {
                dp[i][j] = dp[i - 1][j - arr[i - 1]] || dp[i - 1][j];
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
        cout<<endl;
    }
    cout<<"Partition possible: "<<dp[n][target]<<endl;
    
}
int main(){
    int arr[]={1,5,11,5};
    int n=sizeof(arr)/sizeof(arr[0]);
    canPartitionToEqualSum(arr,n);
    return 0;
}