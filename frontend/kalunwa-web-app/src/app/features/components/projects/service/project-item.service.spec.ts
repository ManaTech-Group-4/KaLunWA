import { TestBed } from '@angular/core/testing';

import { ProjectItemService } from './project-item.service';

describe('ProjectItemService', () => {
  let service: ProjectItemService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ProjectItemService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
