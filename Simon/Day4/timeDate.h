#ifndef timeIncludeGuard
#define timeIncludeGuard

#include <iostream>

using namespace std;


class timeDate {

private:
	int year;
	int month;
	int day;
	int hour;
	int min;

public:

	timeDate(int year, int month,  int day, int hour, int min) {
		this->year = year;
		this->month = month;
		this->day = day;
		this->hour = hour;
		this->min = min;

	}
	~timeDate() {};

	 int get_year() const { return year; }
	 int get_month() const { return month; }
	 int get_day() const { return day; }
	 int get_hour() const { return hour; }
	 int get_min() const { return min; }

	void set_year(int year) { this->year = year; }
	void set_month() { this->month = month; }
	void set_day() { this->day = day; }
	void set_hour() { this->hour = hour; }
	void set_min() { this->min = min; }

	//return true if earlier, else return false
	bool operator<(const timeDate& time) const {
		
		if (year > time.get_year()) return false;
		else if (year < time.get_year()) return true;
		
		else if (month > time.get_month()) return false;
		else if (month < time.get_month()) return true;

		else if (day > time.get_day()) return false;
		else if (day < time.get_day()) return true;

		else if (hour > time.get_hour()) return false;
		else if (hour < time.get_hour()) return true;

		else if (min > time.get_min()) return false;
		else if (min < time.get_min()) return true;
		
		return false;
	}

	void print() {
		cout << year << "-" << month << "-" << day << "-" << "-" << hour << "-" << min << endl;
	}

};


#endif