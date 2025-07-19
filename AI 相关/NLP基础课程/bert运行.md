```SQL
python bert-master/run_classifier.py \
  --task_name=MRPC \
  --do_train=true \
  --do_eval=true \
  --data_dir=GLUE/glue_data/MRPC \
  --vocab_file=GLUE/BERT_BASE_DIR/uncased_L-12_H-768_A-12/vocab.txt \
  --bert_config_file=GLUE/BERT_BASE_DIR/uncased_L-12_H-768_A-12/bert_config.json \
  --init_checkpoint=GLUE/BERT_BASE_DIR/uncased_L-12_H-768_A-12/bert_model.ckpt \
  --max_seq_length=128 \
  --train_batch_size=8 \
  --learning_rate=2e-5 \
  --num_train_epochs=3.0 \
  --output_dir=GLUE/output
python BERT-BiLSTM-CRF-NER-master/run.py \
  -data_dir=BERT-BiLSTM-CRF-NER-master/data \
  -output_dir=BERT-BiLSTM-CRF-NER-master/result \
  -init_checkpoint=BERT-BiLSTM-CRF-NER-master/chinese_L-12_H-768_A-12/bert_model.ckpt \
  -vocab_file=BERT-BiLSTM-CRF-NER-master/chinese_L-12_H-768_A-12/vocab.txt \
  -bert_config_file=BERT-BiLSTM-CRF-NER-master/chinese_L-12_H-768_A-12/bert_config.json \
  -batch_size=8
bert-base-ner-train \
    -data_dir BERT-BiLSTM-CRF-NER/data_set \
    -output_dir BERT-BiLSTM-CRF-NER/output \
    -init_checkpoint BERT-BiLSTM-CRF-NER/uncased_L-12_H-768_A-12/bert_model.ckpt \
    -bert_config_file BERT-BiLSTM-CRF-NER/uncased_L-12_H-768_A-12/bert_config.json \
    -vocab_file BERT-BiLSTM-CRF-NER/uncased_L-12_H-768_A-12/vocab.txt \
    -batch_size 8
bert-base-ner-train 
                [-h] 
                [-data_dir DATA_DIR] 
                [-bert_config_file BERT_CONFIG_FILE] 
                [-output_dir OUTPUT_DIR] [-init_checkpoint INIT_CHECKPOINT]
                [-vocab_file VOCAB_FILE] 
                [-max_seq_length MAX_SEQ_LENGTH] 
                [-do_train] [-do_eval] 
                [-do_predict] 
                [-batch_size BATCH_SIZE]
                [-learning_rate LEARNING_RATE]
                [-num_train_epochs NUM_TRAIN_EPOCHS]
                [-dropout_rate DROPOUT_RATE] [-clip CLIP]
                [-warmup_proportion WARMUP_PROPORTION]
                [-lstm_size LSTM_SIZE]
                [-num_layers NUM_LAYERS]
                [-cell CELL]
                [-save_checkpoints_steps SAVE_CHECKPOINTS_STEPS]
                [-save_summary_steps SAVE_SUMMARY_STEPS]
                [-filter_adam_var FILTER_ADAM_VAR]
                [-do_lower_case DO_LOWER_CASE]
                [-clean CLEAN]
                [-device_map DEVICE_MAP]
                [-label_list LABEL_LIST]
                [-verbose]
                [-ner NER]
                [-version]
```

![](./assets/bert%E8%BF%90%E8%A1%8C/bert%E8%BF%90%E8%A1%8C.png)

![](./assets/bert%E8%BF%90%E8%A1%8C/bert%E8%BF%90%E8%A1%8C-1.png)