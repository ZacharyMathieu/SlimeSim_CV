#ifndef PARAMETERREADER_H
#define PARAMETERREADER_H

#include <vector>
#include <string>

struct InputParam
{
    std::string name;
    std::string valueString;
    double valueNumber;
    bool valueBool;
};

class ParameterReader
{
public:
    static std::vector<InputParam> read(std::string &fileName);
};

#endif // PARAMETERREADER_H
