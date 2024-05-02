from typing import Literal

SPECIAL_VALUE = Literal["+++++++", "Off"]


class ValueContainer:
    def __init__(self, numCH: int = 20, numGS: int = 8) -> None:
        self.numCH = numCH
        self.numGS = numGS
        self.value: list[SPECIAL_VALUE | float] = []
        self.unit: list[str] = []
        self.name: list[str] = []
        for i in range(numCH):
            self.value.append(0)
            self.unit.append("C")
            self.name.append(f"CH {i+1}")
        for i in range(numGS):
            self.value.append(0)
            self.unit.append("degC")
            self.name.append(f"GS {i+1}")

    def SetItem(self, name: str, value: float | SPECIAL_VALUE, unit: str) -> None:
        index = self.name.index(name)
        self.value[index] = value
        self.unit[index] = unit


class DocumentBuilder:
    def __init__(self, valueContainer: ValueContainer = ValueContainer()) -> None:
        self.value: ValueContainer = valueContainer
        self.header = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN""http://www.w3.org/TR/html4/frameset.dtd"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><title>digital</title><style type="text/css">* {font-family: monospace;}</style></head><body>'
        self.TableHeader = "<table border=1><tr>"
        self.TableFooter = "</tr></table>"
        self.footer = "</body></html>"

    def buildDocument(self) -> str:
        text = self.header
        text += self.TableHeader
        for i in range(len(self.value.name)):
            text += self.buildTableElement(self.value.name[i], self.value.value[i], unit=self.value.unit[i])
        text += self.TableFooter
        text += self.footer
        return text

    def buildTableElement(self, channel_name: str, value: str | float, unit: str) -> str:
        if type(value) is float:
            if value >= 0:
                value = f"+ {value:.1f}"
            else:
                value = f"- {value:.1f}"
        return f"<td><table height=90 width=155 border=1 cellpadding=0 cellspacing=0 bgcolor=white><tr><td><font size=4 color=#0068b8><b>&nbsp;{channel_name}</b></font></td></tr><tr><td><font size=6 color=#0068b8><b>&nbsp;{value}</b></font></td></tr><tr><td><font size=4 color=#0068b8><b>&nbsp;{unit}</b></font></td></tr></table></td>"


builder = DocumentBuilder()

print(builder.buildDocument())
