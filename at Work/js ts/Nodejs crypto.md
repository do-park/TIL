# Nodejs crypto

- 암호화된 출력에는 임의성(randomness)이 있어야 한다.
- Initialize Vector(IV)
  - 초기화 벡터
  - 암호화 알고리즘에 IV를 추가해 임의성을 얹을 수 있고, 이 임의성은 암호화가 매번 다른 결과를 만들 수 있도록 도와준다.
  - 암호 해싱의 salt와 유사

```javascript
import crypto from 'crypto';

const ENCRYPTION_KEY = process.env.ENCRYPTION_KEY || ''; // Must be 256 bits (32 characters)
const IV_LENGTH = 16; // For AES, this is always 16

export const encrypt = (text) => {
  const iv = crypto.randomBytes(IV_LENGTH);
  const cipher = crypto.createCipheriv(
    'aes-256-cbc',
    Buffer.from(ENCRYPTION_KEY),
    iv,
  );
  const encrypted = cipher.update(text);

  return (
    `${iv.toString('hex')
    }:${
      Buffer.concat([encrypted, cipher.final()]).toString('hex')}`
  );
};

export const decrypt = (text) => {
  const textParts = text.split(':');
  const iv = Buffer.from(textParts.shift(), 'hex');
  const encryptedText = Buffer.from(textParts.join(':'), 'hex');
  const decipher = crypto.createDecipheriv(
    'aes-256-cbc',
    Buffer.from(ENCRYPTION_KEY),
    iv,
  );
  const decrypted = decipher.update(encryptedText);

  return Buffer.concat([decrypted, decipher.final()]).toString();
};
```

- 참고: console.firebase.google.com/u/0/