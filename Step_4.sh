#!/bin/bash
cd tensorflow-for-poets-2

python -m tensorflow.python.tools.optimize_for_inference \
  --input=tf_files/retrained_graph.pb \
  --output=tf_files/optimized_graph.pb \
  --input_names="input" \
  --output_names="final_result"

du -h tf_files/optimized_graph.pb

gzip -c tf_files/optimized_graph.pb > tf_files/optimized_graph.pb.gz

gzip -l tf_files/optimized_graph.pb.gz

python -m scripts.quantize_graph \
  --input=tf_files/optimized_graph.pb \
  --output=tf_files/rounded_graph.pb \
  --output_node_names=final_result \
  --mode=weights_rounded

gzip -c tf_files/rounded_graph.pb > tf_files/rounded_graph.pb.gz

gzip -l tf_files/rounded_graph.pb.gz


python -m scripts.evaluate  tf_files/optimized_graph.pb

python -m scripts.evaluate  tf_files/rounded_graph.pb

cp tf_files/rounded_graph.pb android/tfmobile/assets/graph.pb

cp tf_files/retrained_labels.txt android/tfmobile/assets/labels.txt 
