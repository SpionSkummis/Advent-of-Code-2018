#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <regex>

using namespace std;

void gridFunc(int fromLeft, int fromTop, int width, int height, int* grid);
bool gridFuncFindNoOverlap(int fromLeft, int fromTop, int width, int height, int* grid);

int main() {

	ifstream* input = new ifstream("./input3.txt");

	vector<string>* inputVector = new vector<string>;
	string inputString;

	int size = 1000 * 1000;
	int* grid = new int[size];

	for (int i = 0; i < size; i++) {
		grid[i] = 0;
	}

	//Regex

	regex IDRegex("\#[0-9]+\ ");
	regex fromLeftRegex("\@\ ([0-9]+)\,");
	regex fromTopRegex("\,([0-9]+)\: ");
	regex widthRegex("\ ([0-9]+)x");
	regex heightRegex("x([0-9]+)");

	smatch resultID;
	smatch resultFromLeft;
	smatch resultFromTop;
	smatch resultWidth;
	smatch resultHeight;


	if (input->is_open()) {
		while (getline(*input, inputString, '\n')) {
			inputVector->push_back(inputString);

			regex_search(inputString, resultID, IDRegex);
			regex_search(inputString, resultFromLeft, fromLeftRegex);
			regex_search(inputString, resultFromTop, fromTopRegex);
			regex_search(inputString, resultWidth, widthRegex);
			regex_search(inputString, resultHeight, heightRegex);

			gridFunc(stoi(resultFromLeft[1].str()), stoi(resultFromTop[1].str()), stoi(resultWidth[1].str()), stoi(resultHeight[1].str()), grid);
			
		}
	}

	int count = 0;
	for (int i = 0; i < 1000000; i++) {	
		if (grid[i] >= 2) count++;	
	}

	cout << "All overlapping inches are  " << count << endl;

	for (auto it = inputVector->begin(); it != inputVector->end(); it++) {

		regex_search(*it, resultID, IDRegex);
		regex_search(*it, resultFromLeft, fromLeftRegex);
		regex_search(*it, resultFromTop, fromTopRegex);
		regex_search(*it, resultWidth, widthRegex);
		regex_search(*it, resultHeight, heightRegex);

		if (gridFuncFindNoOverlap(stoi(resultFromLeft[1].str()), stoi(resultFromTop[1].str()), stoi(resultWidth[1].str()), stoi(resultHeight[1].str()), grid)) {
			cout << "ID that has no overlap is  " << resultID[0].str() << endl;
			
		}

	}

	std::system("pause");

	return 0;

}


void gridFunc(int fromLeft, int fromTop, int width, int height, int* grid) {

	int k = 1000;

	for (int h = fromTop; h < (height + fromTop); h++) {
		for (int w = fromLeft; w < (width + fromLeft); w++) {

			grid[h*k + w]++;
		}
	}
}

	bool gridFuncFindNoOverlap(int fromLeft, int fromTop, int width, int height, int* grid) {

		int k = 1000;

		for (int h = fromTop; h < (height + fromTop); h++) {
			for (int w = fromLeft; w < (width + fromLeft); w++) {

				grid[h*k + w]++;
				if (grid[h*k + w] > 2) return false;

			}


		}
		return true;
	}




