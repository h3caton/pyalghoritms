""" 
Sortowanie przez scalanie
"""

class Sort:

    @classmethod
    def sort(cls, array):
        tmp_len = len(array)/2
        if len(array) > 1:
            tmp1 = array[0:tmp_len]
            tmp2 = array[tmp_len:]
            t1 = Sort.sort(tmp1)
            t2 = Sort.sort(tmp2)
            return cls.merge(t1,t2)
        else:
            return array

    @classmethod
    def merge(cls, t1, t2):
        ret = []
        while len(t1) or len(t2):
            if len(t1) and len(t2):
                if t1[0] < t2[0]:
                    ret.append(t1.pop(0))
                else:
                    ret.append(t2.pop(0))
            else:
                if len(t1):
                    ret+=t1
                    break
                if len(t2):
                    ret+=t2
                    break
        return ret


if __name__ == '__main__':
    print Sort.sort([7,3,4,8,9,2,1])

