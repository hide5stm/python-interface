
from mspy import obj_peak
from mspy import obj_peaklist
from mspy import obj_scan

def deisotope(mzData, iData):
    data = []
    for index, curMZ in enumerate(mzData):
        data.append([curMZ, iData[index]])

    buff = []
    for point in data:
        buff.append(obj_peak.peak(point[0], point[1]))

    scanData = obj_scan.scan(peaklist=obj_peaklist.peaklist(buff))

    scanData.peaklist.deisotope()
    result = []
    for p in scanData.peaklist:
        result.append(p.isotope)
    return result
    