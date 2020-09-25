def test_main(mocker):
    # include_router = mocker.patch("correction_adaptor.main.app.include_router")
    # message_router = mocker.patch("correction_adaptor.main.message.router")

    from .main import app

    # include_router.assert_called_once_with(message_router)
    # TODO how to make this work?
