#include <iostream>
#include <vector>

using namespace std;

bool find(vector<int> arr, int value) {
    for (int i = 0; i < sizeof(arr); i++) {
        if (arr[i] == value) return true;
    }
    return false;
}

vector<int> sort(vector<int> arr, vector<char> answer) {
    
    vector<int> final_;
    int answer_size = answer.size();

    final_.assign(answer_size, 0);
    for (int i = 0; i < answer_size; i++) { final_[i] = i; }

    for (int k = 0; k < answer_size; k++) {
        if (find(arr, answer[k])) {
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

int main() {
    const string ANSWER = "smog";
    vector<char> v_ANSWER(ANSWER.begin(), ANSWER.end());
    vector<int> guess;
    vector<int> sorted;

    for (int i = 0; i < v_ANSWER.size(); i++) {
        cout << "_";
    }
    cout << endl;

    do {
        guess.push_back(getInput("Guess: "));
        
        sorted = sort(guess, v_ANSWER);
        cout << "\n"+wordFactory(sorted)+"\n";

    } while (find(sorted, -1));

    return 0;
}
