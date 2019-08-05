biaobei_dir = "../Downloads/BZNSYP"
biaobei_label_dir = "../Downloads/BZNSYP/ProsodyLabeling/000001-010000.txt"
biaobei_biaodian_dir = "../Downloads/BZNSYP/ProsodyLabeling/daibiaodian.txt"
biaobei_label_output = "../Downloads/BZNSYP/metadata.txt"
biaobei_biaodian_output = "../Downloads/BZNSYP/metadata_biaodian.txt"

# Initialize output files
temp_file = open(biaobei_label_output, 'w')
temp_file.close()
temp_file = open(biaobei_biaodian_output, 'w')
temp_file.close()

# Write metadata
task_pairs = [(biaobei_label_dir, biaobei_label_output), (biaobei_biaodian_dir, biaobei_biaodian_output)]
for task_pair in task_pairs:
    with open(task_pair[0], 'r') as file:
        lines = file.readlines()
        assert len(lines) == 20000
        single_indicator = True
        filename = ""
        for line in lines:
            if single_indicator:
                filename = line.split('\t')[0]
            else:
                with open(task_pair[1], 'a') as output:
                    content = filename + "|" + line.replace('\t', '')
                    output.write(content)
            single_indicator = not single_indicator

print("Task DONE")





