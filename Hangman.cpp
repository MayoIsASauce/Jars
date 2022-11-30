#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

template <typename T>
bool find(vector<T> arr, T value) {
    for (int i = 0; i < sizeof(arr); i++) {
        if (arr[i] == value) return true;
    }
    return false;
}

string printChars(vector<int> arr) {
    string final_;
    
    final_ = final_ + "{ ";
    for (int i = 0; i < arr.size(); i++) {
        final_ += char(arr[i]);
        final_ += ',';
        final_ += ' ';
    }
    final_ += "}";

    return final_;
}

vector<int> sort(vector<int> arr, vector<char> answer) {
    
    vector<int> final_;
    int answer_size = answer.size();

    final_.assign(answer_size, 0);
    for (int i = 0; i < answer_size; i++) { final_[i] = i; }

    for (int k = 0; k < answer_size; k++) {
        if (find<int>(arr, answer[k])) {
            final_[k] = answer[k];
        }
        else {
            final_[k] = -1;
        }
    }

    return final_;
}

string wordFactory(vector<int> ordinal) {
    string word = "";

    for (int i = 0; i < ordinal.size(); i++) {
        char letter;
        if (ordinal[i] < 0) letter = '_';
        else letter = char(ordinal[i]);

        word = word + letter;
    }

    return word;
}

int getInput(string message) {
    char in;
    cout << message;
    cin >> in;

    return in;
}

string hang_man(int level) {
    string man = "";

    for (int n = 0; n < 8; n++) { 
        for (int n2 = 0; n2 < 8; n2++) {
            man += " ";
        }
        man += "\n";
    }

    man[0] = '+';
    for (int i = 0; i < 6; i++) {
        man[9+(9*i)] = '|';
    }
    man[54] = '+';

    switch (level)
    {
        case 8:
            man[51] = '\\';
        case 7:
            man[49] = '/';
        case 6:
            man[33] = '/';
        case 5:
            man[31] = '\\';
        case 4:
            man[32] = '|';
            man[41] = '|';
        case 3:
            man[23] = 'O';
        case 2:
            man[14] = '|';
        case 1:
            for (int i = 0; i < 4; i++) {
                man[1+i] = '-';
            }
            man[5] = '+';
            break;
    
    default:
        break;
    }

    for (int i = 0; i < 6; i++) {
        man[55+i] = '-';
    }

    return man;
}

string selectWord() {
    ifstream myfile ("words_EC.txt");
    vector<string> lines;

    int count = 0;
    while ( !myfile.eof() && myfile.is_open() ) { // always check whether the file is open
        lines.push_back("");
        myfile >> lines[count]; // pipe file's content into stream
        count++;
    }

    srand(time(NULL));
    return lines[rand()%(lines.size())];
}

void recordResults(string message) {
    ofstream result_file;
    result_file.open("results_EC.txt", ios::app);

    result_file << message << endl;
    result_file.close();
}

int main() {
    string ANSWER = selectWord();
    vector<char> v_ANSWER(ANSWER.begin(), ANSWER.end());
    vector<int> guess;
    vector<int> sorted;
    sorted.assign(v_ANSWER.size(), -1);
    int mistakes = 0;

    cout << hang_man(mistakes) << endl;
    for (int i = 0; i < v_ANSWER.size(); i++) {
        cout << "_";
    }
    cout << endl;

    recordResults("The choosen word is " + ANSWER + "\n");

    do {
        guess.push_back(getInput("Guess: "));
        string res = "The character ";
        res += char(guess.back());

        if (!find<char>(v_ANSWER, guess.back())) {
            mistakes++;
            recordResults(res + " was not found! The error count is " + to_string(mistakes));
        } else {
            sorted = sort(guess, v_ANSWER);
            recordResults(res + " was found!");
        }

        cout << "Mistakes: " << mistakes << endl;


        cout << "\n"+hang_man(mistakes)+"\n"+wordFactory(sorted)+"\n"+printChars(guess)+"\n";

    } while (find(sorted, -1) && mistakes < 8);

    if (mistakes > 7) {
        recordResults("\nThe user failed to find the word.");
    } else {
        recordResults("\nThe user successfully found the word.");
    }
    return 0;
}
