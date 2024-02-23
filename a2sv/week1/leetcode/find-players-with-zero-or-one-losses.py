class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic = {}
        no_loss =list()
        loss1 = list()
        
        for i in range(len(matches)):
            if matches[i][1] in dic:
                dic[matches[i][1]] +=1
            else:
                dic[matches[i][1]] = 1
        for i in range(len(matches)):
            if matches[i][0] not in dic and matches[i][0] not in no_loss:
                no_loss.append(matches[i][0])
            if matches[i][1] not in dic and matches[i][1] not in no_loss:
                no_loss.append(matches[i][1])
            elif matches[i][1] in dic and dic[matches[i][1]]==1:
                loss1.append(matches[i][1])
                dic[matches[i][1]] += 1
            elif matches[i][0] in dic and dic[matches[i][0]]==1:
                loss1.append(matches[i][0])
                dic[matches[i][0]] += 1

        return [sorted(no_loss), sorted(loss1)]