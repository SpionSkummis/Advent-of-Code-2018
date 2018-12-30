#include <iostream>
#include <vector>
#include <regex>
#include <string>
#include <fstream>
#include <map>
#include <time.h>
#include <deque>
#include <algorithm>


using namespace std;

int removePairs(string inputString);

int main() {

	clock_t t = clock();
	
	ifstream* input = new ifstream("../input5.txt");
	string inputString;
	string modifiedInputString = "" ;

	vector<int> minSize;
	

	if (input->is_open()) {
		getline(*input, inputString, '\n');
	}

	cout << "Removes all illegal pairs: " << (removePairs(inputString)) << endl;;
	
	for (char alph = 'a'; alph < 'z'; alph++) {
		
		modifiedInputString = "";

		for (char c : inputString) {
			if (c != alph && c != (alph + ('A' - 'a'))) {
				modifiedInputString.push_back(c);
			}
		}
		cout << (removePairs(modifiedInputString)) << endl;;
		cout << alph << "  Length of resulting string: " << modifiedInputString.size() <<  "  Time: " << (double)clock() / CLOCKS_PER_SEC << endl;
	}



	cout << "  Time: " <<  (double)clock() / CLOCKS_PER_SEC << endl;
	system("pause");
	return 0;

}


int removePairs(string inputString) {
	deque<char>* result = new deque<char>;
	for (char c : inputString) {
		if (result->empty()) result->push_back(c);
		else {
			char prevChar = result->back();
			if (abs(prevChar - c) == abs('A' - 'a')) {
				result->pop_back();
			}
			else result->push_back(c);
		}
	}

	return result->size();

}

/*

regex regex("aA|Aa|bB|Bb|cC|Cc|dD|Dd|eE|Ee|fF|Ff|gG|Gg|hH|Hh|iI|Ii|kK|Kk|jJ|Jj|lL|Ll|mM|Mm|nN|Nn|oO|Oo|pP|Pp|qQ|Qq|rR|Rr|sS|Ss|tT|Tt|uU|Uu|vV|Vv|wW|Ww|xX|Xx|yY|Yy|zZ|Zz"); //
smatch result;

int size = inputString.size();
while (true) {
	cout << inputString.size() << endl;

	inputString = regex_replace(inputString, regex, "");


	if (size == inputString.size()) break;
	size = inputString.size();


	cout << "Time: " << (float)clock() / CLOCKS_PER_SEC << endl;
}
*/