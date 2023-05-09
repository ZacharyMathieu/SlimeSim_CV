#include "ParameterReader.h"
#include "Constants.h"

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <windows.h>

std::vector<InputParam> ParameterReader::read(std::string &fileName) {
    const char delimiter = PARAMETER_DELIMITER;

    auto pList = std::vector<InputParam>();

    TCHAR buffer[MAX_PATH] = {0};
    GetModuleFileName(nullptr, buffer, MAX_PATH);
    std::string path = std::string(buffer) + R"(\..\SlimeSim\)" + fileName;

    std::ifstream file;
    file.open(path);

    if (file.is_open()) {
        std::string str;
        while (std::getline(file, str)) {
            std::vector<std::string> out;
            std::stringstream ss(str);
            std::string s;
            while (std::getline(ss, s, delimiter)) {
                out.push_back(s);
            }

            if (out.size() >= 2) {
                InputParam param = {
                        .name = out[0]
                };
                try {
                    double d = std::stod(out[1]);
                    param.valueNumber = d;
                } catch (std::invalid_argument &e) {
                    if (out[1] == "true") {
                        param.valueBool = true;
                    } else if (out[1] == "false") {
                        param.valueBool = false;
                    } else {
                        param.valueString = out[1];
                    }
                }
                pList.push_back(param);
            }
        }
    } else {
        std::cout << "FILE FAILED TO OPEN: [" << path << "]" << std::endl;
    }

    file.close();

    return pList;
}
