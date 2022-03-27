import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';
import { TotalDemographicsModel } from '../models/demographics-total-model';

import { AboutpageService } from './aboutpage.service';

describe('AboutpageService', () => {
  let service: AboutpageService,
      httpTestingController: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [
        AboutpageService
      ]
    });
    service = TestBed.get(AboutpageService);
    httpTestingController = TestBed.get(HttpTestingController);
  });


  afterEach(()=>{
    httpTestingController.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });


  it('should retrieve total Demographics', () => {
    const testMembers: TotalDemographicsModel =
    {total_members: 100};

    service.getDemographics().subscribe((member)=>{
      expect(testMembers).toBe(member,'should check mocked data');
    });

    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/about-us/demographics');

    expect(req.cancelled).toBeFalsy();
    expect(req.request.responseType).toEqual('json');

    req.flush(testMembers);

  });
});
