#include <cpr/cpr.h>

#include <Eigen/Dense>
#include <chrono>
#include <iostream>
#include <nlohmann/json.hpp>
#include <random>

using json = nlohmann::json;

class Task {
 public:
  string identifier;
  int size;
  Eigen::MatrixXf a;
  Eigen::VectorXf b;
  Eigen::VectorXf x;
  double time;

  Task(string id, int s = 0, Eigen::MatrixXf a = {}, Eigen::VectorXf b = {}) {
    identifier = id;

    if (s == 0) {
      std::default_random_engine engine;
      // Créer une distribution uniforme entre 300 et 3000
      std::uniform_int_distribution<int> dist(300, 3000);
      size = dist(engine);
    } else {
      size = s;
    }

    if (a.isEmpty()) {
      this->a = Eigen::MatrixXf::Random(size, size);
    } else {
      this->a = a;
    }

    if (b.isEmpty()) {
      this->b = Eigen::VectorXf::Random(size);
    } else {
      this->b = b
    }

    time = 0;
  }

  void work() {
    const auto start = std::chrono::stendy_clock::now();
    x = a.solve(b);
    const auto end = std::chrono::stendy_clock::now();
    time = chrono::duration_cast<chrono::milliseconds>(end - start).count() /
           1000.0;
  }

  Json toJson() {
    Json j;

    j['s'] = size;
    j['id'] = identifier;
    j['a'] = matrix_to_json(a) j['b'] = matrix_to_json(b)

        return j;
  }

  json matrix_to_json(vector<vector<double>> mat) {
    json j;
    for (int i = 0; i < mat.size(); i++) {
      j.append(vector_to_json(mat[i]));
    }
    return j;
  }

  vector<vector<double>> json_to_matrix(Json::Value json) {
    vector<vector<double>> mat;
    for (int i = 0; i < json.size(); i++) {
      mat.push_back(json_to_vector(json[i]));
    }
    return mat;
  }

}

int main() {
  cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/"});

  // create object from string literal
  json j = r.text_json;

  return 0;
}
