#include "time.h"
#include "event.h"
#include "guard.h"
#include <iostream>
#include <vector>
#include <regex>
#include <string>
#include <fstream>
#include <map>

using namespace std;

int main() {

	ifstream* input = new ifstream("./input4.txt");
	
	string inputString;

	vector<timeDate>* timeVector = new vector<timeDate>;
	vector<event>* eventVector = new vector<event>;
	map<int,guard>* guardMap = new map<int,guard>;

	regex wakeRegex("wakes up");
	regex startShiftRegex("Guard #([0-9]+) begins shift");
	regex asleepRegex("falls asleep");

	regex timeRegex("\\[([0-9]{4})\-([0-9]{2})\-([0-9]{2})\ ([0-9]{2})\:([0-9]{2})\\]"); //([0-9]{2})\-([0-9]{2})\ ([0-9]{2})\:([0-9]{2})\]"
	
	smatch resultTime;
	smatch resultShift;
	smatch resultWake;
	smatch resultAsleep;

	int i = 0;
	if (input->is_open()) {
		while (getline(*input, inputString, '\n')) {


			regex_search(inputString, resultTime, timeRegex);
			
			int year = stoi(resultTime[1].str());
			int month = stoi(resultTime[2].str());
			int day = stoi(resultTime[3].str());
			int hour = stoi(resultTime[4].str());
			int min = stoi(resultTime[5].str());

			regex_search(inputString, resultTime, timeRegex);
			if (regex_search(inputString, resultShift, startShiftRegex)) {
				int ID = stoi(resultShift[1].str());
				eventVector->push_back(event(year, month, day, hour, min, ID));
				guardMap->insert(make_pair(ID, guard(ID)));
					
			
			}
			else if (regex_search(inputString, resultWake, wakeRegex)) {
				eventVector->push_back(event(year, month, day, hour, min, 0,0));
				
			}
			else if (regex_search(inputString, resultAsleep, asleepRegex)) {
				eventVector->push_back(event(year, month, day, hour, min, 0, 1));
				
			}
			else {
				
			}
			//if (i == 10) break;
			//i++;
		}
	}

	cout << "*******************************************" << endl;
	sort(eventVector->begin(), eventVector->end());

	/*
	for (auto it = eventVector->begin(); it != eventVector->end(); it++) {
		it->print();
	}
	*/
	/*
	for (auto it = guardSet->begin(); it != guardSet->end(); it++) {
		it->print();
	}

	*/
	
	auto it = eventVector->begin();

	event* curEvent = &(*it);
	int curID = curEvent->ID;
	bool isAwake = true;
	
	it++;
		for (it; it != eventVector->end(); it++) {
			cout << curID << endl;
			
			if (it->ID != 0){
					curID = it->ID;
					curEvent = &(*it);
			
			}
			else if (it->isAsleep) {
				isAwake = false;
				curEvent = &(*it);
			}

			else {  //När en vakt vaknar
				guardMap->at(curID).minutesSleepingGrid(*curEvent->time, *it->time);
				isAwake = true;
				curEvent = &(*it);
			}

		}
	
	
		for (auto it = guardMap->begin(); it != guardMap->end(); it++) {
			it->second.print();
			it->second.mostSleptMinute();
		}
	
		//cout << "\n\n most slept minute:  "  <<  guardMap->at(3187).mostSleptMinute() << endl;
	
	system("PAUSE");
	return 0;


}