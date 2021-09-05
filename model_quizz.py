tp, fp, fn, tn = [int(x) for x in input().split()]

accuracy = (tp + tn) / (tp + fp + fn + tn)
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * precision * recall / (precision + recall)
score = (accuracy + precision + recall + f1) / 4

print(f"{accuracy:.4}")
print(f"{precision:.4}")
print(f"{recall:.4}")
print (f"{f1:.4}")
