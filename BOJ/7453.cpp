#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


vector<int> generate_possible_case(vector<int>& A, vector<int>& B) {
    vector<int> result;

    for (auto a : A) {
        for (auto b : B) {
            result.push_back(a + b);
        }
    }
    return result;

}

long long get_count(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
    vector<int> AB = generate_possible_case(A, B);
    vector<int> CD = generate_possible_case(C, D);
    sort(AB.begin(), AB.end());
    sort(CD.begin(), CD.end());
    long long count = 0;

    for (auto num : AB) {
        count += (long long)(upper_bound(CD.begin(), CD.end(), -num) - lower_bound(CD.begin(), CD.end(), -num));
    }

    return count;

}


int main()
{
    int N;
    cin >> N;
    vector<int> A(N);
    vector<int> B(N);
    vector<int> C(N);
    vector<int> D(N);

    for (int i = 0; i < N; i++)
    {
        cin >> A[i] >> B[i] >> C[i] >> D[i];
    }

    cout << get_count(A, B, C, D);

    return 0;
}