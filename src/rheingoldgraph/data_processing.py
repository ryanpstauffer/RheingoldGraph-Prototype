"""Data processing module for RheingoldGraph.

Some MIDI conversion logic built off Magenta project.
magenta.scripts.convert_dir_to_note_sequences.py
"""

import os

import tensorflow as tf

from magenta.models.melody_rnn.melody_rnn_create_dataset import get_pipeline
from magenta.models.melody_rnn import melody_rnn_model
# from magenta.scripts.convert_dir_to_note_sequences import convert_midi
from magenta.pipelines import pipeline
from magenta.music import midi_io
from magenta.pipelines import statistics
from rheingoldgraph.pipelines import get_midi_to_melody_proto_pipeline


def run_pipeline_once(pipeline, input_iterator):
    """Generate that runs a pipeline and yields the output.

    Use this instead of `magenta.pipelines.pipeline.run_pipeline_serial()`
    to generate a dataset on the fly, without saving it disk
    or holding the entire dataset in memory.

    Args:
        pipeline: A Pipeline instance.
        input_iterator: Iterates over the input data. Items returned by it are fed
            directly into the pipeline's `transform` method.
    
    Yields:
        Instances of the return values of pipeline.transform.
    """ 
    # This doesn't guarantee a dict right now!
    total_inputs = 0
    total_outputs = 0
    stats = []
    input_iterator = list(input_iterator)
    # print(len(input_iterator))
    # print(input_iterator)
    for input_object in input_iterator:
        # print(input_object)
        total_inputs += 1
        
        # print(len(input_object))
        # print(type(input_object))
        # print(input_object)
        outputs = pipeline.transform(input_object)
        # for name, output_list in outputs.items()
        # print(outputs) 
        # print(total_inputs)


def convert_midi_dir_to_melody_sequences(root_dir, recurse=False):
    """Generator that converts midi files in a directory to monophonic sequence proto.

    Generator that yields NoteSequences.

    Args:
        root_dir: A string specifying a root directory
        recurse: A boolean specifying whether to recursively add midi files
            to the graph
    """ 
    total_inputs = 0
    total_outputs = 0
    stats = []

    config = melody_rnn_model.default_configs['basic_rnn']

    pipeline_instance = get_midi_to_melody_proto_pipeline(config) 
    # results = pipeline.load_pipeline(pipeline_instance, seq_iter)
    
    # parse melodies
    # melodies = results['melodies']
    # for melody in melodies:
    #    yield melody.to_sequence()


    for midi_name, midi_bytes in midi_file_iterator(root_dir, recurse=recurse):
        outputs = pipeline_instance.transform(midi_bytes)

        melody_seq = outputs['melody_sequence'][0] 
        yield midi_name, melody_seq 


def midi_file_iterator(root_dir, recurse=True):
    """Generator that iterates over all MIDI files in the given directory.

    Will recurse into sub-directories if `recurse` is True.
    Ignore non-MIDI files.
    Derived from magenta.pipelines.pipeline.file_iterator()
 
    Args:
        root_dir: Path to root directory to search for files in.
        recurse: If True, subdirectories will be traversed. Otherwise,
            only files in `root_dir` are opened.
    
    Yields:
        tuple (filename, raw_bytes)

        midi_name: name of the MIDI file.
        raw_bytes: Raw bytes (as a string) of each file opened.
    """
    midi_extensions = ['.midi', '.mid']
    dirs = [os.path.join(root_dir, child)
            for child in tf.gfile.ListDirectory(root_dir)]
    while dirs:
        sub = dirs.pop()
        if tf.gfile.IsDirectory(sub):
            if recurse:
                dirs.extend(
                    [os.path.join(sub, child) for child in tf.gfile.ListDirectory(sub)])
        else:
            if (sub.lower().endswith('.mid') or sub.lower().endswith('.midi')):
                midi_name = sub.replace(root_dir, '').lstrip('/')
                with open(sub, 'rb') as f:
                    yield midi_name, f.read()



def get_melodies_from_sequences(seq_iter):
    """Generator that yields melody sequence protos."""
    config = melody_rnn_model.default_configs['basic_rnn']

    pipeline_instance = get_midi_to_melody_proto_pipeline(config) 
    results = pipeline.load_pipeline(pipeline_instance, seq_iter)
    
    # parse melodies
    melodies = results['melodies']
    for melody in melodies:
        yield melody.to_sequence()

    

if __name__ == "__main__":
    input_dir = '/Users/ryanstauffer/Projects/Rheingold/midi/new_single_test'

    # midi_file_iterator(input_dir)
    test = convert_midi_dir_to_sequences(input_dir, False)
    # seq_iter = convert_midi_dir_to_sequences(input_dir, '', False)
    # 
    # # main section to create dataset
    # config = melody_rnn_model.default_configs['basic_rnn']

    # # Build out pipeline
    # pipeline_instance = get_midi_to_melody_proto_pipeline(config) 

    # results = pipeline.load_pipeline(pipeline_instance, seq_iter)
    # 
    # # parse melodies
    # melodies = results['melodies']
    # sequences = []
    # for melody in melodies:
    #     sequences.append(melody.to_sequence())
    # # run_pipeline_streaming(pipeline_instance, seq_iter) 
