from apps.common.util.exception_handler import HandleExceptions
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ContactSerializer


class BaseContactView(APIView):
    """
    スコアに関連する操作のためのスーパークラス。
    """

    permission_classes = [AllowAny]

    @HandleExceptions()
    def post(self, request, *args, **kwargs):
        """
        POSTメソッドでスコア関連のリクエストを処理。

        Args:
            request: HTTPリクエストオブジェクト。
        Returns:
            Response: 成功時はスコアに関する情報が含まれたレスポンス。
        """
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = self.handle_request(serializer.validated_data)
        return Response(response_data, status=status.HTTP_200_OK)

    def handle_request(self, validated_data):
        """
        サブクラスで実装されるべきリクエストデータ処理ロジック。

        Args:
            validated_data: バリデーションを通過したリクエストデータ。
        Raises:
            NotImplementedError: サブクラスで実装が必要な場合に発生。
        Returns:
            dict: 処理結果を返す辞書。
        """
        raise NotImplementedError(
            "サブクラスはhandle_requestメソッドを実装する必要あり"
        )

    def format_response(self, response_data, status="success", message=None):
        """
        レスポンスデータを共通のフォーマットで整形する。

        Args:
            response_data: レスポンスデータ
            status: レスポンスのステータス（デフォルトは"success"）。
            message: エラーメッセージなど、オプションのメッセージ。

        Returns:
            dict: フォーマットされたレスポンスデータ
        """
        response = {"status": status}

        # メッセージがあれば追加
        if message:
            response["message"] = message

        # `data` キーを使わずにレスポンスデータを直接追加
        response.update(response_data)

        return response