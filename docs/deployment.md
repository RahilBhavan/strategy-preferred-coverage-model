# Deployment receipt

Published October 16, 2026. This record describes the first successful deployment.

- Repository: https://github.com/RahilBhavan/strategy-preferred-coverage-model
- Project page: https://rahilbhavan.github.io/strategy-preferred-coverage-model/
- Textbook: https://rahilbhavan.github.io/strategy-preferred-coverage-model/textbook.html
- Deployment run: https://github.com/RahilBhavan/strategy-preferred-coverage-model/actions/runs/38928423199
- Deployed content commit: `25bf16a234fd101282002584261efe5d78eb9ac7`.
- Deployed workbook SHA-256: `fbb1e455fe3e176d618eb3f4b87681be123a6f3638a8a4b6411b8f6ce574710b`.

The downloaded public workbook matches the local final file by SHA-256. The deployed textbook calculator was exercised: changing net mNAV to 0.8x changes static coverage from 15.2 to 3.1 years; no broken internal anchors were found. A script-assembly issue found in the first repository commit was corrected before the successful deployment. The initial deploy failed before Pages was enabled; the linked run deployed successfully after configuration.

No connected Microsoft Excel session was available when document sessions were checked. Native Mac verification and Goal Seek are still pending. Q3 refresh and the human reader responses are also pending. Publication of this educational site does not imply approval of an X post or application submission.

Later deployments: the Pages workflow redeployed `site/` on October 19, 2026 (commit `096efc4`, run [39273786908](https://github.com/RahilBhavan/strategy-preferred-coverage-model/actions/runs/39273786908)). That run changed the textbook only. On October 21, 2026, the downloaded public workbook still had the SHA-256 above, and the live `textbook.html` matched `site/textbook.html` byte for byte.
