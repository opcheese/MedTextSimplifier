import gpt_2_simple as gpt2
import os
import sys

def gpt2_finetuning(model_name, data_file, step):
    if not os.path.isdir(os.path.join("models", model_name)):
        print(f"Downloading {model_name} model...")
        gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/

    sess = gpt2.start_tf_sess()
    file_name = data_file
    '''
   	For finetuning use this command. Following are other parameters of the finetuning function:
        sess,
        dataset,
        steps=-1,
        model_name='124M',
        model_dir='models',
        combine=50000,
        batch_size=1,
        learning_rate=0.0001,
        accumulate_gradients=5,
        restore_from='latest',
        run_name='run1',
        checkpoint_dir='checkpoint',
        sample_every=100,
        sample_length=1023,
        sample_num=1,
        multi_gpu=False,
        save_every=1000,
        print_every=1,
        max_checkpoints=1,
        use_memory_saving_gradients=False,
        only_train_transformer_layers=False,
        optimizer='adam',
        overwrite=False
    '''
    gpt2.finetune(sess,
            file_name,
            model_name=model_name,
            run_name='run'+str(step),
            batch_size=4,
            checkpoint_dir='checkpoint',
            steps=step)   # steps is max number of training steps

def main():
    if len(sys.argv) < 4:
    	print('[usage] python gpt2_finetuning.py model_name, data_file step')
    	return None
    gpt2_finetuning(sys.argv[1], sys.argv[2], int(sys.argv[3]))
	
if __name__ == '__main__':
    main()