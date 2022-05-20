import { TestBed } from '@angular/core/testing';

import { CollectivePagesService } from './collective-pages.service';

describe('CollectivePagesService', () => {
  let service: CollectivePagesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CollectivePagesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
