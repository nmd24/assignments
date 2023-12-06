#include<iostream>
#include<string>
#include<vector>
using namespace std;

vector<vector<int>> generate(int numRows)
{
        vector<vector<int>> result;
        for(auto i=0;i<numRows;++i)
        {
                   result.push_back(vector<int>(i+1,1));
                 for(auto j=1; j<i; ++j)
                 {
                         result[i][j] = result[i-1][j-1] + result[i-1][j];
                 }
          }
          return result;
}

int main()
{
    int numRows;
    cout << "Enter value of n: " ;
    cin >> numRows;
    cout << endl;
    cout << "Pascal triangle for " << numRows << " row value is: " <<endl << endl;
        vector<vector<int> > result = generate(numRows);
        for (int i = 0; i < result.size(); i++)
    {
            for (int j = 0; j < result[i].size(); j++)
            {
                    cout<< result[i][j]<<" ";
            }
            cout<<endl;
    }
}
