
import sys
from pprint import pprint


def index_samples_by_class(
	class_labels	# integer array of sample labels
):
	# check if all ints?
	if not all(isinstance(item, int) for item in class_labels):
		print_error('index_samples()','invalid class labels')
		return False

	# number of classes is the largest label+1
	num_classes = max(class_labels)+1
	# empty list for each class
	class_index = [[] for i in range(num_classes)]
	# assign indexes, force all negative labels to be same class
	for i in range(len(class_labels)):
		class_index[
			class_labels[i] if class_labels[i] > 0 else 0
		].append(i)

	return class_index


def stratified_cv(
	num_folds,
	class_index, # samples indexed by class
	sample_mask # indicate which samples are used
):

	return True


def print_error(
	trace,
	msg
):
	print('!!error: '+trace+': '+msg)

def print_warning(
	trace,
	msg
):
	print('!warning: '+trace+': '+msg)

def main():
	class_labels = [-1,-1,1,1,-1,2,2,-3]
	class_index = index_samples_by_class(class_labels)
	if not class_index:
		print_error('cv.py','cannot index samples')
		sys.exit(1)

	pprint(class_index)


if __name__ == '__main__':
	main()

