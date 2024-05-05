from typing import Literal, Self

SPECIAL_VALUE = Literal["+++++++", "Off"]
DATA_PER_ROW = 3


class ColorWheel:
    def __init__(self) -> None:
        self.index = 0
        self.max_col = DATA_PER_ROW
        self.col = ["#e02830", "#0068b8", "#48b040", "#a800a8", "#e08010", "#28b8f0", "#f0b808", "#e00088", "#885838", "#98d800"]

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> str:
        if self.index >= self.max_col:
            self.index = 0
        else:
            self.index += 1
        return self.col[self.index - 1]


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
        self.colwheel = ColorWheel()

    def buildDocument(self) -> str:
        text = self.header
        text += self.TableHeader
        index = 0
        for i in range(len(self.value.name) // DATA_PER_ROW):
            text += "<tr><td>"
            for j in range(DATA_PER_ROW):
                text += self.buildTableElement(self.value.name[index], self.value.value[index], unit=self.value.unit[i], col=next(self.colwheel))
                index += 1
            text += "</td></tr>"
        text += self.footer
        return text

    def buildTableElement(self, channel_name: str, value: str | float, unit: str, col: str) -> str:
        if type(value) is float:
            if value >= 0:
                value = f"+ {value:.1f}"
            else:
                value = f"- {value:.1f}"
        return f"<td><table height=90 width=155 border=1 cellpadding=0 cellspacing=0 bgcolor=white><tr><td><font size=4 color={col}><b>&nbsp;{channel_name}</b></font></td></tr><tr><td><font size=6 color={col}><b>&nbsp;{value}</b></font></td></tr><tr><td><font size=4 color={col}><b>&nbsp;{unit}</b></font></td></tr></table></td>"


builder = DocumentBuilder()

print(builder.buildDocument())
