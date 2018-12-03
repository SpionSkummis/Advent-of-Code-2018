// basic file operations
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

int sumOfVector(vector<int>*);

int main() {

	ifstream* freqChange = new ifstream("./input1.txt");
	string numberString;
	vector<int>* freqVector = new vector<int>();
	unordered_set<int>* repFreqSet = new unordered_set<int>();

	int* freq;
	
	if (freqChange->is_open()) {


		while (getline(*freqChange, numberString, '\n')){
			freqVector->push_back(stoi(numberString));
			
		}
	}

	int freqSum = 0;
	repFreqSet->insert(0);

	auto it = freqVector->begin();
	int n = 0;  //Number of loops

	while (true) {
		if (it == freqVector->end()) {
			n++;
			it = freqVector->begin();
		}
		freqSum += *it;
		

		if (repFreqSet->count(freqSum)) {
	
			break;
		}
		
		it++;
		repFreqSet->insert(freqSum);
	}


	cout << "This is the sum of the input frequency  freq: " << sumOfVector(freqVector) << endl;
	cout << "This is the repeating freq: " << freqSum << endl;

	std::system("pause");
	return 0;


}

int sumOfVector(vector<int>* vector) {
	int sum = 0;
	for (auto it = vector->begin(); it != vector->end(); it++) {
		sum += *it;
	}
	return sum;
}

