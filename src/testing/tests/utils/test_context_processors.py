from battlehack.utils.context_processors import config


def test_config_context_processor(rf):
    context = config(rf.get('/'))

    assert len(context) == 1
    assert 'DEBUG' in context
