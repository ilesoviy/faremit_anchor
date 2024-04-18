from rest_framework.request import Request
from polaris.models import Asset

def toml_contents(request, *args, **kwargs): 
  asset = Asset.objects.first()
  # asset2 = Asset.objects.last()

  return {
    "DOCUMENTATION":
      {
        "ORG_NAME": "LINK.IO LTD.",
        "ORG_DBA": "LINK",
        "ORG_URL": "https://www.linkio.africa/",
        "ORG_LOGO": "https://uploads-ssl.webflow.com/60a70a1080cf2974d4b1595e/60b623a4d06b3b67a49c9e82_WEBCLIP.png",
        "ORG_DESCRIPTION": "LINK is a Global Cross Border payments platform for the next billion Africans, providing services in a Faster and Cheaper way",
        "ORG_PHYSICAL_ADDRESS": "2 Fredrick Street, Kings Cross, London, United Kingdom WC1X 0ND",
        "ORG_TWITTER": "link_io",
        "ORG_OFFICIAL_EMAIL": "support@linkupio.com",
        "ORG_GITHUB": "linkioafrica",
      },
    "PRINCIPALS": [
      {
        "name": "Evarist Emmanuel",
        "email": "engremmanuelec@gmail.com"
      },
      {
        "name": "Tomisin Leshi",
        "email": "tomisinleshi@gmail.com"
      }
    ],
    "CURRENCIES": [
      {
        "code": asset.code,
        "issuer": asset.issuer,
        "name": "USD",
        "desc": "The official currency of the United States of America",
        "display_decimals": 2,
        "is_asset_anchored": "true",
        "is_unlimited": "true",
        "anchor_asset_type": "fiat",
        "anchor_asset": "USD",
        "redemption_instructions": "contact Authorized Dealers or signup with KYC info on LINK",
        "status": "test",
        "image": "https://ipfs.io/ipfs/bafkreibpzncuhbk5ozhdw7xkcdoyf3xhwhcwcf6sj7axjzimxw6vm6pvyy"
      },
      # {
      #   "code": asset2.code,
      #   "issuer": asset2.issuer,
      #   "name": "USD Coin",
      #   "display_decimals": 2,
      #   "is_asset_anchored": "true",
      #   "is_unlimited": "true",
      #   "anchor_asset_type": "fiat",
      #   "anchor_asset": "USD",
      #   "status": "test",
      # }
    ]
  }
