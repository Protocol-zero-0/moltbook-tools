import * as fs from 'fs';
import * as crypto from 'crypto';

/**
 * Identity Lock - Ensures agent identity persistence and tamper detection.
 * Protocol Zero Standard.
 */

interface IdentityConfig {
  agentId: string;
  signature: string;
  timestamp: number;
}

const IDENTITY_FILE = './.identity.lock';

export class IdentityLock {
  private config: IdentityConfig | null = null;

  constructor() {
    this.loadIdentity();
  }

  private loadIdentity() {
    if (fs.existsSync(IDENTITY_FILE)) {
      const data = fs.readFileSync(IDENTITY_FILE, 'utf-8');
      this.config = JSON.parse(data);
    }
  }

  public generateIdentity(agentId: string, secret: string): void {
    const timestamp = Date.now();
    const signature = crypto
      .createHmac('sha256', secret)
      .update(`${agentId}:${timestamp}`)
      .digest('hex');

    this.config = { agentId, signature, timestamp };
    fs.writeFileSync(IDENTITY_FILE, JSON.stringify(this.config, null, 2));
    console.log(`[IdentityLock] Identity generated for ${agentId}`);
  }

  public verifyIdentity(secret: string): boolean {
    if (!this.config) {
      console.error('[IdentityLock] No identity found.');
      return false;
    }

    const { agentId, signature, timestamp } = this.config;
    const expectedSignature = crypto
      .createHmac('sha256', secret)
      .update(`${agentId}:${timestamp}`)
      .digest('hex');

    const isValid = signature === expectedSignature;
    console.log(`[IdentityLock] Verification result: ${isValid ? 'VALID' : 'INVALID'}`);
    return isValid;
  }
}

// Usage Example
// const lock = new IdentityLock();
// lock.generateIdentity('Protocol-Zero', 'super-secret-key');
// lock.verifyIdentity('super-secret-key');
