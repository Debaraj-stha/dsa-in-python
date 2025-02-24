#include<iostream>
#include<vector>
#include<unordered_map>
#include<numeric>
using namespace std;
void display(const vector<int> arr){
    for(int num : arr){
        cout<<num<<" ";
    }
    cout<<endl;
}
void subArrayWithZeroSum(const vector<int> arr){
    unordered_map<int,vector<int>> sumMap;
    vector<vector<int>> subArrays;
    int currentSum=0;
    sumMap[0].push_back(-1);
    for(int i=0;i<arr.size();i++){
        currentSum+=arr[i];
        if(sumMap.find(currentSum)!=sumMap.end()){
            for(int index:sumMap[currentSum]){
                vector<int> temp(arr.begin()+index+1,arr.begin()+i+1);
                subArrays.push_back(temp);
            }

        }
        sumMap[currentSum].push_back(i);
    }
    cout<<"Subarrays with zero sum: "<<endl;
    for(const auto& sub:subArrays){
        display(sub);
        cout<<"Sum: "<<accumulate(sub.begin(),sub.end(),0)<<endl;
        cout<<"--------"<<endl;
    }

}
int main() {
    vector<int> arr = {1, 2, -3, 3, -3, 12, 17, -17, 18, 90, 9, -9};
    display(arr);
    subArrayWithZeroSum(arr);
    return 0;
}
