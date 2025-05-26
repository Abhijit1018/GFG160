#include <algorithm>
#include <iostream>
#include <vector>
#include <iterator>

using namespace std;

int main()
{
    vector<int> arr = { 2,4,1,7,5,0 };
    next_permutation(arr.begin(), arr.end());
    for (int num : arr)
        std::cout << num << " ";
    return 0;
}
