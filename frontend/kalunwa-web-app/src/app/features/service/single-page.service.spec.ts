import { TestBed } from '@angular/core/testing';

import { SinglePageService } from './single-page.service';

describe('SinglePageService', () => {
  let service: SinglePageService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SinglePageService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
