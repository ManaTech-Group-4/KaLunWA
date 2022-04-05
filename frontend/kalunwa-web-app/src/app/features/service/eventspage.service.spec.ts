import { TestBed } from '@angular/core/testing';

import { EventspageService } from './eventspage.service';

describe('EventspageService', () => {
  let service: EventspageService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EventspageService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
