from urllib import parse
from django import template
from django.shortcuts import resolve_url

register = template.Library()

# 検索結果を保持してページネーションを表示する
@register.simple_tag
def url_replace(request, field, value):
    """GETパラメータを一部を置き換える"""

    url_dict = request.GET.copy()
    url_dict[field] = str(value)
    return url_dict.urlencode()

# 戻るリンク
@register.simple_tag
def get_return_link(request):
    top_page = resolve_url('list')  # listページ
    referer = request.environ.get('HTTP_REFERER')  # 前ページのURL

    # URL直接入力やお気に入りアクセスのときはリファラがないので、トップぺージに戻す
    if referer:

        # リファラがある場合、前回ページが自分のサイト内であれば、そこに戻る
        parse_result = parse.urlparse(referer)
        if request.get_host() == parse_result.netloc:
            return referer

    return top_page