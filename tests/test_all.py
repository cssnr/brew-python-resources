from unittest.mock import patch

import pytest

from brewresources.cli import main


def test_cli(capsys):
    with patch("sys.argv", ["bpr", "-V"]):
        with pytest.raises(SystemExit):
            main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "0.0.1"

    with patch("sys.argv", ["bpr"]):
        with pytest.raises(SystemExit):
            main()
    captured = capsys.readouterr()
    assert captured.err.strip() == "Error: Package [name] is required. Use --help for more details."

    # with patch("sys.argv", ["bpr", "-C"]):
    #    with pytest.raises(SystemExit):
    #        main()
    #    captured = capsys.readouterr()
    #    assert captured.out == "Cache Cleared.\n"

    with patch("sys.argv", ["bpr", "rich"]):
        main()
        captured = capsys.readouterr()
        assert "mdurl" in captured.out
